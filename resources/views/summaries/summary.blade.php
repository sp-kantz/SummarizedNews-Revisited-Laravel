@extends('layouts.app')
    
@section('content')


    <h1>Summary page</h1>
    <div>
        @if (count($summary)>0)
            
        <h2>{{$summary[0]->summary_title}}</h2>

        <div>
        @foreach ($sources as $source)

            <a href="{{$source->url}}">{{$source->title}}</a>

        @endforeach
        </div>

        @else
            <p>Error. No summary found</p>
        @endif
    </div>

@endsection
        
            