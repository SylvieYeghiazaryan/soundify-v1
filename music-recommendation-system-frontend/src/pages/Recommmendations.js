import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchSongs } from "../store/slices/songsSlice";
import Filters from "../components/Filters";
import SongList from "../components/SongList";
import SearchBar from "../components/SearchBar";
import { Typography } from "antd";
import { CustomerServiceOutlined, PlayCircleOutlined } from "@ant-design/icons";

const { Title } = Typography;

const Recommendations = () => {
    const userId = useSelector((state) => state.auth.userId);
    const dispatch = useDispatch();
    const [genre, setGenre] = useState("");
    const [mood, setMood] = useState("");

    useEffect(() => {
        if (userId) {
            dispatch(fetchSongs(userId, { genre, mood }));
        }
    }, [userId, genre, mood, dispatch]);

    return (
        <div style={styles.page}>
            <div style={styles.header}>
                <div style={styles.iconWrapper}>
                    <CustomerServiceOutlined style={styles.icon} />
                    <Title level={1} style={styles.appName}>Soundify</Title>
                    <PlayCircleOutlined style={styles.icon} />
                </div>
            </div>

            <div style={styles.controls}>
                <SearchBar />
                <Filters setGenre={setGenre} setMood={setMood} />
            </div>

            <SongList />
        </div>
    );
};

const styles = {
    page: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "20px",
        minHeight: "100vh",
        background: "#FF6F61",
        fontFamily: "Arial, sans-serif",
    },
    header: {
        textAlign: "center",
        marginBottom: "20px",
    },
    iconWrapper: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
    },
    icon: {
        fontSize: "40px",
        color: "#fff",
        margin: "0 10px",
    },
    appName: {
        color: "#fff",
        fontSize: "3rem",
        fontFamily: "'Lobster', cursive",
        margin: "0",
    },
    controls: {
        display: "flex",
        justifyContent: "center",
        width: "100%",
        gap: "15px",
        marginBottom: "20px",
    },
};

export default Recommendations;


