@extends('layouts.app')

@section('header_title', 'Dashboard')

@section('content')
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-18">
            <div class="card">
            
                <div class="card-body">
                    @if (session('status'))
                        <div class="alert alert-success" role="alert">
                            {{ session('status') }}
                        </div>
                    @endif

                    <a class="btn btn-primary" href="/summaries">Home</a>

                    <hr>
                    <h3>Your Comment History</h3>
                    <table class="table table-striped">
                        <tr>
                            <td><label>Comment</label></td>
                            <td>News Summary</td>
                            <td>Date</td>
                        </tr>
                        <td>
                        </td>
                            
                            @foreach ($comments as $comment)
                                <tr>
                                    <td><p>{{$comment->comment_text}}</p></td>
                                <td><a href="/summaries/{{$comment->summary_id}}">{{$comment->summary_title}}</a></td>
                                <td>{{$comment->created_at}}</td>
                                </tr>
                            @endforeach
                            
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
