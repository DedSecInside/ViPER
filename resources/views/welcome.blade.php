<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>ViPER™ - Pen Tester</title>

        <!-- Fonts -->
        <link href="https://fonts.googleapis.com/css?family=Coming+Soon" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Gloria+Hallelujah" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Audiowide" rel="stylesheet">
        <!-- Styles -->
        <style>
        .count{
            font-family: 'Audiowide', cursive;
            color: white;
        }
            html, body {
                background:url('/images/viper2.jpg');
                background-repeat:no-repeat;
                background-position: center;
                background-size: cover;
                color: gold;
                font-family: 'Coming Soon', cursive;
                font-weight: 100;
                height: 100vh;
                margin: 0;
            }

            .full-height {
                height: 100vh;
            }

            .flex-center {
                align-items: center;
                display: flex;
                justify-content: center;
            }

            .position-ref {
                position: relative;
            }

            .top-right {
                position: absolute;
                right: 10px;
                top: 18px;
            }

            .content {
                text-align: center;
            }

            .title {
                font-size: 84px;
            }

            .links > a {
                color: white;
                padding: 0 25px;
                font-size: 12px;
                font-weight: 600;
                letter-spacing: .1rem;
                text-decoration: none;
                text-transform: uppercase;
                border: 1px solid white;
            }

            .m-b-md {
                margin-bottom: 30px;
            }
            .title{
                font-size: 120px;
                font-family: 'Gloria Hallelujah', cursive;
            }
        </style>
    </head>
    <body>
        <div class="flex-center position-ref full-height">
            @if (Route::has('login'))
                <div class="top-right links">
                    @if (Auth::check())
                        <a href="{{ url('/home') }}">Home</a>
                    @else
                        <a href="{{ url('/login') }}">Login</a>
                        <a href="{{ url('/register') }}">Register</a>
                    @endif
                </div>
            @endif

            <div class="content">
                <div class="title m-b-md">
                    ViPER<span style="font-size:20px;">™</span>
                </div>

                <div class="links">
                    <a href="#">Documentation</a>
                    <a href="https://github.com/DedSecInside/">GitHub</a>
                </div>
                <h2 class="count">{{$count}}+ Scans Completed and Counting!</h2>
            </div>
        </div>
    </body>
</html>
