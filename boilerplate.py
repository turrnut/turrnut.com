writeTo = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Turrnut</title>
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="icon" type="image/x-icon" href="../icon/turrnut.ico">
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar">
        <a href="../" class="logo">
            <img src="../icon/turrnut.png" alt="Logo Icon" class="logo-icon">
            Turrnut
        </a>
        <button class="hamburger" id="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <ul class="nav-links" id="nav-links">
            <li><a href="../">Home</a></li>
            <li><a href="https://www.youtube.com/@turrnut" target="_blank">YouTube</a></li>
            <li><a href="../blogs/">Blog</a></li>
            <li><a href="../turrnesian/">Turrnesian</a></li>
            <li><a href="../about/">About</a></li>
        </ul>
    </nav>
    
    
    
    
    <!-- STUFF -->

    <br/>
    <br/>
    <br/>
    <br/>

    <!-- Footer -->
    <footer class="footer">
        Copyright (c) Turrnut 2025
    </footer>

    <script src="../js/script.js"></script>
</body>
</html>
"""

with open("example.html", "w") as fobj:
    fobj.write(writeTo)
