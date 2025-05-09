import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const authSlice = createSlice({
    name: "auth",
    initialState: { userId: null },
    reducers: {
        setUser: (state, action) => {
            state.userId = action.payload;
        },
        logoutUser: (state) => {
            state.userId = null;
        },
    },
});

export const { setUser, logoutUser } = authSlice.actions;

/**
 * Asynchronous action to handle user login.
 * Sends a POST request with username and password.
 * On success, sets the user ID in the Redux state.
 */
export const login = (username, password) => async (dispatch) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/login/", { username, password });
        dispatch(setUser(response.data.user_id));
    } catch (error) {
        console.error("Login failed:", error);
    }
};

export default authSlice.reducer;
