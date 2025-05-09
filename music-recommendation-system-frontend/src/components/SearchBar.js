import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { fetchSearchResults } from "../store/slices/songsSlice";
import { Input, Button } from "antd";
import { SearchOutlined } from "@ant-design/icons";

/**
 * A search bar that allows users to input natural language queries to search for songs.
 * Dispatches the search query to Redux, which fetches the relevant results from the backend.
 */
const SearchBar = () => {
    const [query, setQuery] = useState("");
    const dispatch = useDispatch();

    /**
     * Handles the search form submission.
     * Dispatches the query to Redux if it's not empty.
     */
    const handleSearch = (e) => {
        e.preventDefault();
        if (query.trim()) {
            dispatch(fetchSearchResults(query));
        }
    };

    return (
        <form onSubmit={handleSearch} style={styles.form}>
            <Input
                placeholder="Tell me what you're in the mood for... "
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                style={styles.input}
                allowClear
            />
            <Button
                type="primary"
                htmlType="submit"
                icon={<SearchOutlined />}
                style={styles.button}
            >
                Search
            </Button>
        </form>
    );
};

const styles = {
    form: {
        display: "flex",
        gap: "10px",
        width: "100%",
        maxWidth: "400px",
        marginBottom: "20px",
    },
    input: {
        flex: 1,
    },
    button: {
        backgroundColor: "#FFA07A",
        borderColor: "#FFA07A",
    },
};

export default SearchBar;



