@extends('layouts.app')

@section('header_title', 'About')

@section('header_links')
    <link href="{{ URL::asset('css/about.css') }}" rel="stylesheet">
@endsection
    
@section('content')

    <article class="container" id="about">

        <h3>About Summarized News</h3>

    
        <div class="article_text" id="about_text">
            <p>Developed as part of my thesis on Extractive Multi-Document Summarization.
            </p>
            <p>The system collects news articles from the web,
                automatically extracts summaries from multiple articles with overlapping content
                and presents the summaries to the users.
            </p>
            <p>The system extracts and presents two summaries for every event or topic described in the
                articles, by applying two different extractive summarization techniques.
                The first technique is based on latent semantic analysis (LSA), 
                and the second on a graph representation of the text. 
            </p>
        </div>
    </article>

@endsection
        
            