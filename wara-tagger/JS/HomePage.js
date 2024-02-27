import React, { useState    } from "react";
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text,TouchableOpacity, View, TextInput, Alert } from 'react-native';

export function Home() {
    const [untagged, setUntagged] = useState("")

    const show = () => {
        Alert.alert(untagged)
    }

    return (
        <View style={styles.container}>
            <TextInput placeholder="Word" 
                style={styles.input_style}
                onChangeText={(newText) => setUntagged(newText)}
            />
            <TouchableOpacity onPress={show}>
                <Text> Submit </Text>
            </TouchableOpacity>
            <StatusBar style="auto" />
        </View>
    );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20
  },
  input_style : {
    padding: 10,
    backgroundColor: "#F9F9F9",
    width: "100%",
    borderRadius: 10
  }
});
