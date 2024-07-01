import React, {Component} from "react";
import {API_URL} from "../constants";
import axios from "axios";

class Home extends Component {
  state = {
    garden: []
  }

  componentDidMount() {
    axios.get(API_URL + "gardens/")
      .then(res => {
        const garden = res.data;
        this.setState({ garden });
      })
  }

  render() {
    return (
      <ul>
        {
          this.state.garden
            .map(garden =>
              <li key={garden.id}>{garden.name}</li>
            )
        }
      </ul>
    )
  }
}


export default Home;
