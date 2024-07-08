import './index.css';
import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from "./components/Header";
import GardensPage from "./pages/GardensPage";
import AboutPage from "./pages/AboutPage";
import LoginPage from "./pages/LoginPage";
import GardenDetailsPage from "./pages/GardenDetailsPage";
import RegistrationPage from "./pages/RegistrationPage";



export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path="/" element={<GardensPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegistrationPage />} />
          <Route path="/garden/:key" element={<GardenDetailsPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}
