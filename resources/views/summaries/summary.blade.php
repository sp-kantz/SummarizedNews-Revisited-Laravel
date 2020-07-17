@extends('layouts.app')
    
@section('content')

    <article>
        @if (count($summary)>0)
            
        <h2>{{$summary[0]->summary_title}}</h2>

        <div class="article_textarea">

            <h5>Graph-based Summary</h5>
            <article class="article_text">
                {{$summary[0]->summary_graph}}
            </article>

            <h5>LSA-based Summary</h5>
            <article class="article_text">
                {{$summary[0]->summary_LSA}}
            </article>
        </div>

        <div>
            <h5>Sources</h5>
            <ul>
            @foreach ($sources as $source)

                <li><a href="{{$source->url}}">{{$source->title}}</a></li>

            @endforeach
            </ul>
        </div>

        @else
            <p>Error. No summary found</p>
        @endif
    </article>

@endsection
        
            