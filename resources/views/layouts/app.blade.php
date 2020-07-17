<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="{{asset('css/app.css')}}">
        
        <link rel="stylesheet" href="{{asset('css/main.css')}}">

        <title>Summarized News | @yield('header_title')</title>

        @yield('header_links')
    </head>
    <body>
        
        @include('layouts.navbar')

        @yield('content')
                
    </body>
</html>
