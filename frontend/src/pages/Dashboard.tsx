import React from "react";
import {
  Container,
  Box,
  Typography,
  Paper,
  Grid,
  Button,
  Card,
  CardContent,
  CardActions,
} from "@mui/material";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";

const Dashboard: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/login");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  const handleManageUsers = () => {
    navigate("/users");
  };

  const handleViewReports = () => {
    navigate("/reports");
  };

  const handleSystemSettings = () => {
    navigate("/settings");
  };

  const handleEditProfile = () => {
    navigate("/profile");
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Grid container spacing={3}>
        {/* Welcome Section */}
        <Grid item xs={12}>
          <Paper
            sx={{
              p: 3,
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <Box>
              <Typography variant="h4" component="h1" gutterBottom>
                Welcome, {user?.first_name}!
              </Typography>
              <Typography variant="subtitle1" color="text.secondary">
                Role: {user?.role}
              </Typography>
            </Box>
            <Button variant="outlined" color="primary" onClick={handleLogout}>
              Logout
            </Button>
          </Paper>
        </Grid>

        {/* User Info Card */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                User Information
              </Typography>
              <Typography variant="body1">
                <strong>Username:</strong> {user?.username}
              </Typography>
              <Typography variant="body1">
                <strong>Email:</strong> {user?.email}
              </Typography>
              <Typography variant="body1">
                <strong>Full Name:</strong> {user?.first_name} {user?.last_name}
              </Typography>
              <Typography variant="body1">
                <strong>Account Created:</strong>{" "}
                {new Date(user?.created_at || "").toLocaleDateString()}
              </Typography>
            </CardContent>
            <CardActions>
              <Button size="small" color="primary" onClick={handleEditProfile}>
                Edit Profile
              </Button>
            </CardActions>
          </Card>
        </Grid>

        {/* Quick Actions Card */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                Quick Actions
              </Typography>
              <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
                {(user?.role === "ADMIN" || user?.role === "SUPER_ADMIN") && (
                  <Button
                    variant="contained"
                    color="primary"
                    onClick={handleViewReports}
                  >
                    View Reports
                  </Button>
                )}
                {user?.role === "SUPER_ADMIN" && (
                  <Button
                    variant="contained"
                    color="secondary"
                    onClick={handleManageUsers}
                  >
                    Manage Users
                  </Button>
                )}
                {user?.role === "SUPER_ADMIN" && (
                  <Button
                    variant="contained"
                    color="info"
                    onClick={handleSystemSettings}
                  >
                    System Settings
                  </Button>
                )}
              </Box>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
