
import React, { Component } from 'react';
import {Helmet} from "react-helmet";
import {Button, Jumbotron} from "react-bootstrap";

class Home extends Component {
    render() {
        return (
            <Jumbotron>
                <Helmet>
                    <title>monograph</title>
                </Helmet>
                <h1 className="display-4">Welcome to monograph!</h1>
                <p className="lead">Monograph is a service to help you find and extract summaries and relationships
                between different research papers. Right now it's in an extremely experimental state.</p>
                <hr className="my-4" />
                <p>Check back later for demos and example results.</p>
                <p className="lead">
                    <Button variant="primary">Learn more</Button>
                </p>
            </Jumbotron>
        );
    }
}

export default Home;