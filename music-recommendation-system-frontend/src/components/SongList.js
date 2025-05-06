import React from "react";
import { useSelector } from "react-redux";
import { Card, Typography } from "antd";

const { Text } = Typography;

const SongList = () => {
    const songs = useSelector((state) => state.songs.list);

    return (
        <div style={styles.listContainer}>
            {songs.length > 0 ? (
                songs.map((song, index) => (
                    <Card key={index} style={styles.card} hoverable>
                        <Text strong style={styles.title}>{song.title}</Text>
                        <Text type="secondary" style={styles.artist}>{song.artist}</Text>
                    </Card>
                ))
            ) : (
                <Text style={styles.noSongs}>No songs available</Text>
            )}
        </div>
    );
};

const styles = {
    listContainer: {
        display: "grid",
        gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))",
        gap: "20px",
        width: "80%",
        maxWidth: "1000px",
    },
    card: {
        padding: "15px",
        textAlign: "center",
        background: "#fff",
        boxShadow: "0 4px 10px rgba(0, 0, 0, 0.1)",
        borderRadius: "10px",
    },
    title: {
        fontSize: "16px",
        display: "block",
    },
    artist: {
        fontSize: "14px",
        display: "block",
    },
    noSongs: {
        fontSize: "18px",
        color: "#fff",
    },
};

export default SongList;




