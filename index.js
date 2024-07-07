const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files (e.g., the contact form HTML file)
app.use(express.static(path.join(__dirname, 'public')));

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/mydatabase', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
    console.log('Connected to database');
});

// Define Contact schema
const contactSchema = new mongoose.Schema({
    firstName: String,
    lastName: String,
    email: String,
    message: String
});

// Create Contact model
const Contact = mongoose.model('Contact', contactSchema);

// Route to handle contact form submissions
app.post('/contact', async (req, res) => {
    const { firstName, lastName, email, message } = req.body;

    try {
        const newContact = new Contact({
            firstName,
            lastName,
            email,
            message
        });

        // Save the new contact
        await newContact.save();
        console.log('Contact saved successfully:', newContact);
        // Sending HTML response with JavaScript for pop-up
        res.send(`
            <script>
                alert("Thank you for your message! We will contact you shortly.");
                window.location.href = "/";
            </script>
        `);
    } catch (error) {
        console.error('Error saving contact information:', error);
        res.status(500).send('Error saving contact information.');
    }
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
