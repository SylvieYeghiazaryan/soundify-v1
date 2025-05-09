import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { login } from "../store/slices/authSlice";
import { Form, Input, Button, Typography, Card } from "antd";
import { PlayCircleOutlined, CustomerServiceOutlined } from '@ant-design/icons';

const { Title } = Typography;


/**
 * The Login component provides a form where users can log in with their username and password.
 * Upon submission, it dispatches the login action to authenticate the user.
 */
const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const dispatch = useDispatch();

    /**
     * Handles form submission. Dispatches the login action with username and password.
     */
    const handleSubmit = () => {
        dispatch(login(username, password));
    };

    return (
        <div style={styles.page}>
            <div style={styles.header}>
                <div style={styles.iconWrapper}>
                    <CustomerServiceOutlined style={styles.icon} />
                    <Title level={1} style={styles.appName}>Soundify</Title>
                    <PlayCircleOutlined style={styles.icon} />
                </div>
            </div>
            <Card style={styles.card}>
                <div style={styles.loginTextWrapper}>
                    <Typography.Text style={styles.loginText}>Login</Typography.Text>
                </div>
                <Form layout="vertical" onFinish={handleSubmit} style={styles.form}>
                    <Form.Item label="Username" rules={[{ required: true, message: "Please enter your username!" }]}>
                        <Input value={username} onChange={(e) => setUsername(e.target.value)} />
                    </Form.Item>
                    <Form.Item label="Password" rules={[{ required: true, message: "Please enter your password!" }]}>
                        <Input.Password value={password} onChange={(e) => setPassword(e.target.value)} />
                    </Form.Item>
                    <Form.Item>
                        <Button type="primary" htmlType="submit" block style={styles.button}>Login</Button>
                    </Form.Item>
                </Form>
            </Card>
        </div>
    );
};

const styles = {
    page: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        flexDirection: "column",
        height: "100vh",
        background: "linear-gradient(45deg, #FF6F61, #FFB6C1)",
        fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif",
    },
    header: {
        textAlign: "center",
        marginBottom: "50px",
    },
    iconWrapper: {
        display: "flex",
        justifyContent: "center",
        marginBottom: "20px",
    },
    icon: {
        fontSize: "40px",
        color: "#FF6F61",
        margin: "0 10px",
    },
    appName: {
        color: "#FF6F61",
        fontSize: "3rem",
        fontFamily: "'Lobster', cursive", // Fancy font
        margin: "0",
    },
    loginTextWrapper: {
        textAlign: "center",
        marginBottom: "20px",
    },
    loginText: {
        color: "#FF6F61",
        fontSize: "2rem",
        fontWeight: "bold",
    },
    card: {
        width: "100%",
        maxWidth: "400px",
        boxShadow: "0 4px 20px rgba(0,0,0,0.1)",
        padding: "20px",
        borderRadius: "10px",
        backgroundColor: "#fff",
    },
    form: {
        width: "100%",
    },
    button: {
        backgroundColor: "#FF6F61",
        borderColor: "#FF6F61",
        color: "#ffffff",
        transition: "background-color 0.3s, border-color 0.3s",
    }
};

export default Login;
