import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ZoneManager from './components/ZoneManager';
import RecordForm from './components/RecordForm';
import RecordList from './components/RecordList';
import './styles/main.css';

function App() {
    return (
        <Router>
            <div className="App">
                <h1>DNS Server Management</h1>
                <Switch>
                    <Route path="/" exact component={Dashboard} />
                    <Route path="/zones" component={ZoneManager} />
                    <Route path="/records" component={RecordList} />
                    <Route path="/add-record" component={RecordForm} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;