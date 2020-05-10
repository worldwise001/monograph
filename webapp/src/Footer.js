import React, { Component } from 'react';
import {Link} from "react-router-dom";


class Footer extends Component {
    render() {
        return (
            <footer className="footer">
                <div className="footer-container">
                    <span className="text-muted">
                        Copyright 2020 <a href='https://www.shh.sh'>Sarah Harvey</a> | <Link to='/about'>About</Link>
                    </span>
                </div>
            </footer>
        );
    }
}

export default Footer;