import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { fetchSearchResults } from "../store/slices/songsSlice";
import { Input, Button } from "antd";
import { SearchOutlined } from "@ant-design/icons";

const SearchBar = () => {
    const [query, setQuery] = useState("");
    const dispatch = useDispatch();

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



