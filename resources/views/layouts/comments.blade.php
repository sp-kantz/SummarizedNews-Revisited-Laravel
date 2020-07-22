<div class="container-fluid">

    @if (Auth::guest())
        <a class="btn btn-dark" href="/login">Login to Post a Comment</a>
        
    @else
        <form method="POST" action="{{url('/summaries/' . $summary->id .'/comment')}}">
            @csrf
            <input type="hidden" id="summary_id" name="summary id" value="{{$summary->id}}">
            <input type="hidden" id="summary_title" name="summary title" value="{{$summary->summary_title}}">

            <div class="form-group">
                <div class="col-md-8">       
                    <textarea id="comment" type="text" class="form-control" name="comment_text" rows="3"></textarea>
                    <button type="submit" class="btn btn-primary">
                        {{ __('Comment') }}
                    </button>
                </div>
            </div>
        </form>
    @endif
    
    
    
    <hr>
    
    <div class="panel panel-default">
        <div class="panel-heading">
            <label class="panel-title">Recent Comments ({{count($comments)}}):</label>
        </div>
        <div class="panel-body">
            @if (count($comments)>0)
                <ul class="list-group"> 
                    @foreach ($comments as $comment)     
                        <li class="list-group-item comment_box" id="{{$comment->id}}">
                            <div class="row">
                                <div class="pl-3">
                                    <div class="row">
                                        <div class="mr-3"><strong>{{$comment->user_name}}</strong></div><small><em> on </em>{{$comment->created_at}}</small>
                                        @if (!Auth::guest())
                                            @if (Auth::user()->id == $comment->user_id)
                                                
                                                    <form method="POST" action="{{url('/dashboard/delete/' . $comment->id)}}">
                                                        @csrf
                                                        <button type="submit" class="btn btn-danger btn-xs ml-3 mb-2" title="Delete">
                                                            <span class="glyphicon glyphicon-trash"></span>
                                                        </button>
                                                    </form>
                                                
                                            @endif                     
                                        @endif 
                                    </div>                                
                                    <div class="comment-text" id="comment_text">{{$comment->comment_text}}</div>
                                        
                                </div>
                            </div>
                        </li>
                    @endforeach
                </ul>
            @else
                    <p>No comments yet</p>
            @endif
        </div>
    </div>
    
</div>

