@extends('layouts.app')

@section('content')

    <h1>Latest News</h1>

    @if (count($summaries)>0)
    <div class="container">
        @foreach ($summaries as $summary)

            <a href="/summaries/{{$summary->summary_id}}">{{$summary->summary_title}}</a>
            
        @endforeach

        {{$summaries->links()}}
    </div>
    @else
        <p>No summaries found</p>
    @endif
    

@endsection
        
            