import React, { useState, useEffect } from "react";
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
  Tabs,
  Tab,
  Divider,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Chip,
  CircularProgress,
} from "@mui/material";
import {
  Person as PersonIcon,
  Store as StoreIcon,
  Inventory as InventoryIcon,
  TrendingUp as TrendingUpIcon,
  Settings as SettingsIcon,
  Logout as LogoutIcon,
  Edit as EditIcon,
  Dashboard as DashboardIcon,
  People as PeopleIcon,
  Assessment as AssessmentIcon,
} from "@mui/icons-material";
import { useAuth } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import { authAPI } from "../services/api";

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

function TabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`dashboard-tabpanel-${index}`}
      aria-labelledby={`dashboard-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

const Dashboard: React.FC = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [tabValue, setTabValue] = useState(0);
  const [stats, setStats] = useState({
    totalUsers: 0,
    totalStores: 0,
    totalProducts: 0,
    recentSales: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        // In a real app, you would fetch these from your API
        // For now, we'll use mock data
        setStats({
          totalUsers: 12,
          totalStores: 5,
          totalProducts: 150,
          recentSales: 8,
        });
      } catch (error) {
        console.error("Error fetching stats:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  const handleLogout = async () => {
    try {
      await logout();
      navigate("/login");
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setTabValue(newValue);
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

  const handleManageInventory = () => {
    navigate("/inventory");
  };

  const handleManageStores = () => {
    navigate("/stores");
  };

  const handleViewSales = () => {
    navigate("/sales");
  };

  if (loading) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

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
              background: "linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)",
              color: "white",
            }}
          >
            <Box>
              <Typography variant="h4" component="h1" gutterBottom>
                Welcome, {user?.first_name || user?.username}!
              </Typography>
              <Typography variant="subtitle1">
                Role: {user?.role === "SUPER_ADMIN" ? "Super Admin" : "Admin"}
              </Typography>
            </Box>
            <Button
              variant="outlined"
              color="inherit"
              onClick={handleLogout}
              startIcon={<LogoutIcon />}
            >
              Logout
            </Button>
          </Paper>
        </Grid>

        {/* Stats Cards */}
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ height: "100%" }}>
            <CardContent>
              <Box sx={{ display: "flex", alignItems: "center", mb: 2 }}>
                <PeopleIcon color="primary" sx={{ mr: 1 }} />
                <Typography variant="h6">Users</Typography>
              </Box>
              <Typography variant="h4">{stats.totalUsers}</Typography>
              <Typography variant="body2" color="text.secondary">
                Total registered users
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ height: "100%" }}>
            <CardContent>
              <Box sx={{ display: "flex", alignItems: "center", mb: 2 }}>
                <StoreIcon color="primary" sx={{ mr: 1 }} />
                <Typography variant="h6">Stores</Typography>
              </Box>
              <Typography variant="h4">{stats.totalStores}</Typography>
              <Typography variant="body2" color="text.secondary">
                Active stores
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ height: "100%" }}>
            <CardContent>
              <Box sx={{ display: "flex", alignItems: "center", mb: 2 }}>
                <InventoryIcon color="primary" sx={{ mr: 1 }} />
                <Typography variant="h6">Products</Typography>
              </Box>
              <Typography variant="h4">{stats.totalProducts}</Typography>
              <Typography variant="body2" color="text.secondary">
                Total products
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <Card sx={{ height: "100%" }}>
            <CardContent>
              <Box sx={{ display: "flex", alignItems: "center", mb: 2 }}>
                <TrendingUpIcon color="primary" sx={{ mr: 1 }} />
                <Typography variant="h6">Sales</Typography>
              </Box>
              <Typography variant="h4">{stats.recentSales}</Typography>
              <Typography variant="body2" color="text.secondary">
                Recent transactions
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        {/* Main Content */}
        <Grid item xs={12}>
          <Paper sx={{ width: "100%" }}>
            <Tabs
              value={tabValue}
              onChange={handleTabChange}
              indicatorColor="primary"
              textColor="primary"
              variant="fullWidth"
            >
              <Tab icon={<DashboardIcon />} label="Overview" />
              <Tab icon={<InventoryIcon />} label="Inventory" />
              <Tab icon={<StoreIcon />} label="Stores" />
              <Tab icon={<TrendingUpIcon />} label="Sales" />
              {user?.role === "SUPER_ADMIN" && (
                <Tab icon={<PeopleIcon />} label="Users" />
              )}
              {user?.role === "SUPER_ADMIN" && (
                <Tab icon={<SettingsIcon />} label="Settings" />
              )}
            </Tabs>

            {/* Overview Tab */}
            <TabPanel value={tabValue} index={0}>
              <Grid container spacing={3}>
                <Grid item xs={12} md={6}>
                  <Card>
                    <CardContent>
                      <Typography variant="h6" gutterBottom>
                        User Information
                      </Typography>
                      <List>
                        <ListItem>
                          <ListItemIcon>
                            <PersonIcon />
                          </ListItemIcon>
                          <ListItemText
                            primary="Username"
                            secondary={user?.username}
                          />
                        </ListItem>
                        <ListItem>
                          <ListItemIcon>
                            <PersonIcon />
                          </ListItemIcon>
                          <ListItemText
                            primary="Email"
                            secondary={user?.email}
                          />
                        </ListItem>
                        <ListItem>
                          <ListItemIcon>
                            <PersonIcon />
                          </ListItemIcon>
                          <ListItemText
                            primary="Full Name"
                            secondary={`${user?.first_name || ""} ${
                              user?.last_name || ""
                            }`}
                          />
                        </ListItem>
                        <ListItem>
                          <ListItemIcon>
                            <PersonIcon />
                          </ListItemIcon>
                          <ListItemText
                            primary="Role"
                            secondary={
                              <Chip
                                label={
                                  user?.role === "SUPER_ADMIN"
                                    ? "Super Admin"
                                    : "Admin"
                                }
                                color={
                                  user?.role === "SUPER_ADMIN"
                                    ? "secondary"
                                    : "primary"
                                }
                                size="small"
                              />
                            }
                          />
                        </ListItem>
                        <ListItem>
                          <ListItemIcon>
                            <PersonIcon />
                          </ListItemIcon>
                          <ListItemText
                            primary="Account Created"
                            secondary={
                              user?.created_at
                                ? new Date(user.created_at).toLocaleDateString()
                                : "N/A"
                            }
                          />
                        </ListItem>
                      </List>
                    </CardContent>
                    <CardActions>
                      <Button
                        size="small"
                        color="primary"
                        onClick={handleEditProfile}
                        startIcon={<EditIcon />}
                      >
                        Edit Profile
                      </Button>
                    </CardActions>
                  </Card>
                </Grid>
                <Grid item xs={12} md={6}>
                  <Card>
                    <CardContent>
                      <Typography variant="h6" gutterBottom>
                        Quick Actions
                      </Typography>
                      <Box
                        sx={{
                          display: "flex",
                          flexDirection: "column",
                          gap: 2,
                        }}
                      >
                        <Button
                          variant="contained"
                          color="primary"
                          onClick={handleViewSales}
                          startIcon={<TrendingUpIcon />}
                        >
                          View Sales
                        </Button>
                        <Button
                          variant="contained"
                          color="primary"
                          onClick={handleManageInventory}
                          startIcon={<InventoryIcon />}
                        >
                          Manage Inventory
                        </Button>
                        <Button
                          variant="contained"
                          color="primary"
                          onClick={handleManageStores}
                          startIcon={<StoreIcon />}
                        >
                          Manage Stores
                        </Button>
                        {user?.role === "SUPER_ADMIN" && (
                          <Button
                            variant="contained"
                            color="secondary"
                            onClick={handleManageUsers}
                            startIcon={<PeopleIcon />}
                          >
                            Manage Users
                          </Button>
                        )}
                        {user?.role === "SUPER_ADMIN" && (
                          <Button
                            variant="contained"
                            color="info"
                            onClick={handleSystemSettings}
                            startIcon={<SettingsIcon />}
                          >
                            System Settings
                          </Button>
                        )}
                      </Box>
                    </CardContent>
                  </Card>
                </Grid>
              </Grid>
            </TabPanel>

            {/* Inventory Tab */}
            <TabPanel value={tabValue} index={1}>
              <Typography variant="h5" gutterBottom>
                Inventory Management
              </Typography>
              <Button
                variant="contained"
                color="primary"
                onClick={handleManageInventory}
                sx={{ mb: 2 }}
              >
                Manage Inventory
              </Button>
              <Typography variant="body1">
                View and manage your inventory items, categories, and stock
                levels.
              </Typography>
            </TabPanel>

            {/* Stores Tab */}
            <TabPanel value={tabValue} index={2}>
              <Typography variant="h5" gutterBottom>
                Store Management
              </Typography>
              <Button
                variant="contained"
                color="primary"
                onClick={handleManageStores}
                sx={{ mb: 2 }}
              >
                Manage Stores
              </Button>
              <Typography variant="body1">
                View and manage your store locations, staff, and inventory.
              </Typography>
            </TabPanel>

            {/* Sales Tab */}
            <TabPanel value={tabValue} index={3}>
              <Typography variant="h5" gutterBottom>
                Sales Dashboard
              </Typography>
              <Button
                variant="contained"
                color="primary"
                onClick={handleViewSales}
                sx={{ mb: 2 }}
              >
                View Sales
              </Button>
              <Typography variant="body1">
                Track sales performance, view reports, and analyze trends.
              </Typography>
            </TabPanel>

            {/* Users Tab (Super Admin Only) */}
            {user?.role === "SUPER_ADMIN" && (
              <TabPanel value={tabValue} index={4}>
                <Typography variant="h5" gutterBottom>
                  User Management
                </Typography>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleManageUsers}
                  sx={{ mb: 2 }}
                >
                  Manage Users
                </Button>
                <Typography variant="body1">
                  Create, edit, and manage user accounts and permissions.
                </Typography>
              </TabPanel>
            )}

            {/* Settings Tab (Super Admin Only) */}
            {user?.role === "SUPER_ADMIN" && (
              <TabPanel value={tabValue} index={5}>
                <Typography variant="h5" gutterBottom>
                  System Settings
                </Typography>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleSystemSettings}
                  sx={{ mb: 2 }}
                >
                  Configure Settings
                </Button>
                <Typography variant="body1">
                  Configure system-wide settings, notifications, and
                  integrations.
                </Typography>
              </TabPanel>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
