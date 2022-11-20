import React from "react";
import MainComponent from "./components/Main/Main/Main";
import HomeComponent from "./components/Home/Home/Home";
import { BrowserRouter, Route, Link } from "react-router-dom";
import "./App.css";
import "./index.css";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <Route exact path="/" component={HomeComponent} />
          <Route path="/dashboard" component={MainComponent} />
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
