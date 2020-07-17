@extends('layouts.app')

@section('header_title', $summary[0]->summary_title)

@section('header_links')
    <link href="{{ URL::asset('css/summaries/summary.css') }}" rel="stylesheet">
@endsection

@section('page-header-title', 'article')
    
@section('content')

    <article id="content">
        @if (count($summary)>0)
            
        <h2 id="summary_title">{{$summary[0]->summary_title}}</h2>

        <div class="article_textarea" id="summaries">

            <label id="summary_method">Graph-based Summary</label>
            <article class="article_text" id="summary_text">
                {{$summary[0]->summary_graph}}
            </article>

            <label id="summary_method">LSA-based Summary</label>
            <article class="article_text" id="summary_text">
                {{$summary[0]->summary_LSA}}
            </article>
        </div>

        <div id="sources">
            <label>Sources</label>
            <ul>
            @foreach ($sources as $source)
                <li>
                    <label id="source_domain">{{$source->domain}}</label></br>
                    <a href="{{$source->url}}" id="source_url">{{$source->title}}</a>
                </li>
            @endforeach
            </ul>
        </div>

        @else
            <p>Error. No summary found</p>
        @endif
    </article>

@endsection
        
            