import { createSlice } from "@reduxjs/toolkit";
import axios from "axios";

const songsSlice = createSlice({
    name: "songs",
    initialState: { list: [] },
    reducers: {
        setSongs: (state, action) => {
            state.list = action.payload;
        },
    },
});

export const { setSongs } = songsSlice.actions;

/**
 * Fetches song recommendations for a user.
 * If filters are provided (genre/mood), calls filtered endpoint.
 * Otherwise, fetches general time-of-day based recommendations.
 */
export const fetchSongs = (userId, filters) => async (dispatch) => {
    try {
        let response;
        if (!filters.genre && !filters.mood) {
            response = await axios.get(`http://127.0.0.1:8000/api/recommendations/${userId}/`);
        } else {
            response = await axios.get(`http://127.0.0.1:8000/api/recommendations/filter/${userId}/`, { params: filters });
        }
        dispatch(setSongs(response.data.recommended_songs));
    } catch (error) {
        console.error("Error fetching songs:", error);
    }
};

/**
 * Sends a free-form natural language query to get song recommendations.
 */
export const fetchSearchResults = (query) => async (dispatch) => {
    try {
        const response = await axios.post(`http://127.0.0.1:8000/api/recommendations/search/`,  { query });
        dispatch(setSongs(response.data.recommended_songs));
    } catch (error) {
        console.error("Error fetching search results:", error);
    }
};

export default songsSlice.reducer;
