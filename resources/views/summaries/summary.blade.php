@extends('layouts.app')

@section('header_title', $summary->summary_title)

@section('header_links')
    <link href="{{ URL::asset('css/summaries/summary.css') }}" rel="stylesheet">
@endsection
    
@section('content')

    <article id="content">
        
        <div class="article_textarea" id="summaries">

            <h2 id="summary_title">{{$summary->summary_title}}</h2>
            <small><em>{{$summary->created_at}}</em></small>
            <hr>

            <label id="summary_method">Graph-based Summary</label>
            <article class="article_text" id="summary_text">
                {{$summary->summary_graph}}
            </article>

            </br>

            <label id="summary_method">LSA-based Summary</label>
            <article class="article_text" id="summary_text">
                {{$summary->summary_LSA}}
            </article>

            <hr>       
            @include('layouts.comments')  
        </div>

        @include('layouts.sources')

    </article>
@endsection
                