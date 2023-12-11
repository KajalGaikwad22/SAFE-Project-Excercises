<?php
$host = "localhost";
$port = "5432";  
$dbname = "PDdb";
$user = "postgres";
$password = "Kajal@701";

try {
    $conn = new PDO("pgsql:host=$host;port=$port;dbname=$dbname;user=$user;password=$password");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Check if "name" and "email" keys are set in $_POST
    if (isset($_POST['name'], $_POST['email'])) {
        // Get form data
        $name = $_POST['name'];
        $email = $_POST['email'];

        // Validate the values (add more validation as needed)
        $name = htmlspecialchars($name);
        $email = filter_var($email, FILTER_VALIDATE_EMAIL);

        // SQL to insert data into the database
        $sql = "INSERT INTO chain_members (name, email) VALUES (?, ?)";
        $stmt = $conn->prepare($sql);
        
        // Bind parameters
        $stmt->bindParam(1, $name);
        $stmt->bindParam(2, $email);
        
        // Execute the statement
        $stmt->execute();

        echo "Joined the chain successfully!";
    } else {
        echo "Error: Name and Email are required.";
    }
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}

$conn = null;
?>
