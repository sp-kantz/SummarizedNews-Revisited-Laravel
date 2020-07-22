@extends('layouts.app')

@section('header_title', 'Home')

@section('header_links')
    <link href="{{ URL::asset('css/summaries/index.css') }}" rel="stylesheet">
@endsection

@section('content')

    @if (count($summaries)>0)

        <div class="container" id="summaries">
            @foreach ($summaries as $summary)
                <div id="summary_entry">
                    <a href="/summaries/{{$summary->id}}" id="summary_link">
                        <div id="summary_title">{{$summary->summary_title}}<br>
                            <em><small>{{$summary->created_at}}</small></em>
                        </div>
                    </a> 
                </div> 
            @endforeach            
        </div>
        
        <div class="pagination">
            {{$summaries->links()}}
        </div>

    @else
        <p>No summaries found</p>
    @endif

@endsection
        
            