@extends('layouts.app')

@section('header_title', 'Dashboard')

@section('header_links')
    <link href="{{ URL::asset('css/dashboard.css') }}" rel="stylesheet">
    @if (auth()->user()->id == 1)
        <script src="/js/adminButton.js"></script>
    @endif
@endsection

@section('content')


@if (auth()->user()->id == 1)
    <input id="startButton" onclick="start()" type="button" class="btn btn-dark pull-right" value="Gather and Summarize News">
    <div class="label-info" id="status"></div>
    <br>

    <form method="GET" action="{{url('/exec')}}">
        @csrf
        <button type="submit" class="btn btn-danger" ><small>Delete</small></button>
    </form>
@endif

<div class="container">
    <div class="row justify-content-center">

        <h3>Your Comment History</h3>
        <hr>
    
        <div class="container">
            @if (session('status'))
                <div class="alert alert-success" role="alert">
                    {{ session('status') }}
                </div>
            @endif
                    
            @if(count($comments)>0)
            <table class="table table-striped">
                <tr>
                    <td><label>Comment</label></td>
                    <td>News Summary</td>
                    <td>Date</td>
                </tr>                            
                @foreach ($comments as $comment)
                    <tr>
                        <td><p>{{$comment->comment_text}}</p></td>
                    <td><a href="/summaries/{{$comment->summary_id}}#{{$comment->id}}">{{$comment->summary_title}}</a></td>
                        <td>{{$comment->created_at}}</td>
                        <td>
                            <form method="POST" action="{{url('/dashboard/delete/' . $comment->id)}}">
                                @csrf
                                <button type="submit" class="btn btn-danger" ><small>Delete</small></button>
                            </form>
                        </td>
                    </tr>
                @endforeach
            </table>
            @else
                <p>You have made no comments    </p> 
            @endif
        </div>
    </div>
</div>
@endsection
