import React, { Component } from 'react';
import Nav from "react-bootstrap/Nav";
import Container from "react-bootstrap/Container";
import Navbar from "react-bootstrap/Navbar";
import {NavLink} from "react-router-dom";
import NavbarBrand from "react-bootstrap/NavbarBrand";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {
    faBook, faHighlighter, faSearch, faTools, faUser
} from "@fortawesome/free-solid-svg-icons";


class Header extends Component {
    render() {
        return (
            <Navbar bg='dark' variant='dark'>
                <Container fluid>
                    <NavbarBrand>
                        <NavLink to='/' className='navbar-brand'>{'monograph'}</NavLink>
                    </NavbarBrand>
                    <Nav>
                        <Nav.Item>
                            <NavLink to='/search' className='nav-link' activeClassName='active'><FontAwesomeIcon icon={faSearch} title={'search'} /></NavLink>
                        </Nav.Item>
                        <Nav.Item>
                            <NavLink to='/library' className='nav-link' activeClassName='active'><FontAwesomeIcon icon={faBook} title={'library'} /></NavLink>
                        </Nav.Item>
                        <Nav.Item>
                            <NavLink to='/annotate' className='nav-link' activeClassName='active'><FontAwesomeIcon icon={faHighlighter} title={'annotate'} /></NavLink>
                        </Nav.Item>
                        <Nav.Item>
                            <NavLink to='/preferences' className='nav-link' activeClassName='active'><FontAwesomeIcon icon={faTools} title={'preferences'} /></NavLink>
                        </Nav.Item>
                        <Nav.Item>
                            <NavLink to='/login' className='nav-link' activeClassName='active'><FontAwesomeIcon icon={faUser} title={'login'} /></NavLink>
                        </Nav.Item>
                    </Nav>
                </Container>
            </Navbar>
        );
    }
}

export default Header;