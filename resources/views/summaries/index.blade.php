@extends('layouts.app')
    
@section('content')

    <h1>Summarized News Homepage</h1>
    <div class="well">

        @if (count($summaries)>0)
            @foreach ($summaries as $summary)

                <a href="/summaries/{{$summary->summary_id}}">{{$summary->summary_title}}</a>
                
            @endforeach

            {{$summaries->links()}}
        @else
            <p>No summaries found</p>
        @endif
    </div>

@endsection
        
            