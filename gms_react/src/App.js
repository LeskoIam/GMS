import './index.css';
import Container from 'react-bootstrap/Container';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Header from "./components/Header";
import GardenPage from "./pages/GardenPage";
import AboutPage from "./pages/AboutPage";
import LoginPage from "./pages/LoginPage";



export default function App() {
  return (
    <Container fluid className="App">
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path="/" element={<GardenPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </Container>
  );
}
