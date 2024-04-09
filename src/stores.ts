import { writable } from "svelte/store";

// no good code in sight
export const keysPressed = writable(0);
export const numberErrors = writable(0);
export const numberSuccess = writable(0);
export const streak = writable(0);
