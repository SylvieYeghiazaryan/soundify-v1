import React from "react";
import { Select } from "antd";

const { Option } = Select;

const genres = ["Pop", "Rock", "Hip-Hop", "Jazz", "Classical", "Electronic", "R&B", "Metal", "Country", "Reggae"];
const moods = ["Happy", "Sad", "Energetic", "Relaxed", "Romantic", "Angry", "Focused", "Nostalgic"];

/**
 * The Filters component renders two Select dropdowns for users to filter songs by Genre and Mood.
 *
 * Props:
 * - setGenre: A function to update the selected genre state in the parent component.
 * - setMood: A function to update the selected mood state in the parent component.
 */
const Filters = ({ setGenre, setMood }) => {
    return (
        <div style={styles.filters}>
            <Select
                placeholder="Select Genre"
                onChange={setGenre}
                style={styles.select}
            >
                {genres.map((g) => (
                    <Option key={g} value={g}>{g}</Option>
                ))}
            </Select>
            <Select
                placeholder="Select Mood"
                onChange={setMood}
                style={styles.select}
            >
                {moods.map((m) => (
                    <Option key={m} value={m}>{m}</Option>
                ))}
            </Select>
        </div>
    );
};

const styles = {
    filters: {
        display: "flex",
        gap: "10px",
        marginBottom: "20px",
    },
    select: {
        width: "180px",
    },
};

export default Filters;