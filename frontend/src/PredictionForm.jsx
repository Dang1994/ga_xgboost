import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, ActivityIndicator, StyleSheet } from "react-native";
import axios from "axios";
import Constants from "expo-constants";

const API_URL = Constants.expoConfig?.extra?.apiUrl || "http://127.0.0.1:5000";

const PredictionForm = () => {
  const [formData, setFormData] = useState({
    diameter: "",
    thickness: "",
    angle: "",
    distance: "",
    mandrel: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (field, value) => {
    setFormData({ ...formData, [field]: value });
  };

  const handleSubmit = async () => {
    setError("");
    setPrediction(null);
    setIsLoading(true);

    if (
      !formData.diameter ||
      !formData.thickness ||
      !formData.angle ||
      !formData.distance ||
      !(formData.mandrel === "0" || formData.mandrel === "1")
    ) {
      setError("All fields are required, and Mandrel Type must be 0 or 1.");
      setIsLoading(false);
      return;
    }

    const inputFeatures = [
      parseFloat(formData.diameter),
      parseFloat(formData.thickness),
      parseFloat(formData.angle),
      parseFloat(formData.distance),
      parseInt(formData.mandrel),
    ];

    try {
      const response = await axios.post(`${API_URL}/predict`, {
        features: inputFeatures,
      });
      setPrediction(response.data.prediction);
    } catch (err) {
      console.error("Error during API call:", err);
      setError(err.response?.data?.error || "An error occurred while making the prediction.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Predict Test Result</Text>

      {["diameter", "thickness", "angle", "distance", "mandrel"].map((field) => (
        <TextInput
          key={field}
          placeholder={`Enter ${field}`}
          value={formData[field]}
          onChangeText={(value) => handleChange(field, value)}
          keyboardType={field === "mandrel" ? "numeric" : "decimal-pad"}
          style={styles.input}
          editable={!isLoading}
        />
      ))}

      <TouchableOpacity style={styles.button} onPress={handleSubmit} disabled={isLoading}>
        {isLoading ? <ActivityIndicator color="#FFF" /> : <Text style={styles.buttonText}>Predict</Text>}
      </TouchableOpacity>

      {isLoading && <ActivityIndicator size="large" color="#007BFF" />}
      {prediction !== null && <Text style={styles.result}>Prediction: {prediction}</Text>}
      {error && <Text style={styles.error}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    padding: 20,
    alignItems: "center",
    backgroundColor: "#f8f9fa",
    flex: 1,
  },
  title: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 20,
  },
  input: {
    width: "100%",
    padding: 10,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 5,
    marginBottom: 10,
    backgroundColor: "#fff",
  },
  button: {
    width: "100%",
    padding: 12,
    backgroundColor: "#007BFF",
    borderRadius: 5,
    alignItems: "center",
  },
  buttonText: {
    color: "#FFF",
    fontSize: 16,
    fontWeight: "bold",
  },
  result: {
    fontSize: 18,
    color: "green",
    marginTop: 15,
  },
  error: {
    fontSize: 16,
    color: "red",
    marginTop: 15,
  },
});

export default PredictionForm;
