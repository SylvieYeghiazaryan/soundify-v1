import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../store/slices/authSlice";
import songsReducer from "../store/slices/songsSlice";

export const store = configureStore({
    reducer: {
        auth: authReducer,
        songs: songsReducer,
    },
});