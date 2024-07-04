import './index.css';
import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from "./components/Header";
import GardensPage from "./pages/GardensPage";
import AboutPage from "./pages/AboutPage";
import LoginPage from "./pages/LoginPage";
import GardenPage from "./pages/GardenPage";



export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path="/" element={<GardensPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<Navigate to="/" />} />
          <Route path="/garden/:key" element={<GardenPage />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}
