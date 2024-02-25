import React from "react";
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';
import { Home } from './JS/HomePage';


export default function MainApp() {
    const Stack = createNativeStackNavigator();

    return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="Waray-Waray Pos Tagger" component={Home} options={{
                    headerShown: true
                }}/>
            </Stack.Navigator>
        </NavigationContainer>
    )
}