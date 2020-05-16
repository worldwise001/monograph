
import React, { Component } from 'react';
import {Helmet} from "react-helmet";

class About extends Component {
    render() {
        return (
            <div className="about-div px-3 py-3 pt-md-5 pb-md-4 mx-auto">
                <Helmet>
                    <title>monograph - about</title>
                </Helmet>
                <h1 className="display-4 text-center">About</h1>
                <p className="lead">
                    Monograph is a portal to find research papers and identify relationships between
                    them. It makes use of PDF extraction, summarization, and linking techniques through popular
                    services such as CrossRef, ACM and IEEE Digital libraries, and arXiv. The intent is to aid
                    researchers (primarily in the field of Computer Science) to find relationships faster.
                </p>
                <p className="lead">
                    This source is <a href='https://worldwise001.github.com/monograph'>freely available</a> under
                    the conditions of the <a href='https://github.com/worldwise001/monograph/blob/master/LICENSE'>MIT License</a>.
                </p>
                <p className="lead">
                    This service is provided free of charge with zero ads and zero trackers. If you want to support
                    this work, head on over to <a href='https://www.patreon.com/worldwise001'>Patreon</a>.
                </p>
            </div>
        );
    }
}

export default About;