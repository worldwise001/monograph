import React, {Component} from 'react';
import './App.css';
import Container from "react-bootstrap/Container";
import {BrowserRouter, Switch, Route} from "react-router-dom";

import Header from "./Header";
import Home from "./Home";
import Search from "./Search";
import Library from "./Library";
import Preferences from "./Preferences";
import Annotate from "./Annotate";
import Footer from "./Footer";
import About from "./About";

class App extends Component {
    render() {
        return (
            <BrowserRouter>
                <div>
                    <Header/>
                        <Switch>
                            <Route exact path='/' component={Home}/>
                            <Route path='/search' component={Search}/>
                            <Route path='/library' component={Library}/>
                            <Route path='/annotate' component={Annotate}/>
                            <Route path='/preferences' component={Preferences}/>
                            <Route path='/about' component={About}/>
                        </Switch>
                    <Footer />
                </div>
            </BrowserRouter>
        );
    }
}

export default App;
