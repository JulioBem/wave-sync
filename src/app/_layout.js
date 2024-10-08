import React from "react";
import { Stack } from "expo-router";

export default function Layout() {
  return (
    <Stack
      screenOptions={{
        contentStyle: { backgroundColor: "#fff" },
      }}
      initialRouteName="comunidade"
    >
      <Stack.Screen name="index" options={{ headerShown: false }} />
      <Stack.Screen name="comunidade" options={{ headerShown: false }} />
    </Stack>
  );
}
