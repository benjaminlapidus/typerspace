import React from 'react';
import './App.css';
import Main from './components/Main/MainWrapper/main';
import Home from './components/Home/HomeWrapper/home';

import {BrowserRouter, Route, Link} from 'react-router-dom';

class App extends React.Component {

  render() {
    return (
      <div className="App">
        
      <BrowserRouter>
        <Route exact path="/" component={Home} />
        <Route path="/dashboard" component={Main} />
</BrowserRouter>
      </div>

      );
    }

}

export default App;