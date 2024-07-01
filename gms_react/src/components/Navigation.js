import React, {Component} from "react";
import {BrowserRouter as Router, Link, Route, Routes} from "react-router-dom";
import Home from "./Home"
import About from "./About"

class Navigation extends Component {
    render() {
        return (
            <header className="App-header">
                <Router>
                    <div>
                        <nav>
                            <ul className="nav bg-info">
                                <li className="nav-item">
                                    <Link to="/" className="nav-link link-light">Home</Link>
                                </li>
                                <li className="nav-item">
                                    <Link to="/about" className="nav-link link-light">About</Link>
                                </li>
                            </ul>
                        </nav>

                        {/* A <Switch> looks through its children <Route>s and
                    renders the first one that matches the current URL. */}
                        <Routes>
                            <Route path='/' element={<Home/>}/>
                            <Route path='/about' element={<About/>}/>
                        </Routes>
                    </div>
                </Router>
                </header>
        );
    }
}


export default Navigation;
