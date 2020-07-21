<div class="container-fluid">
    
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
    
    <hr>
    <div class="row">
        <div class="panel panel-default widget w-100">
            <div class="panel-heading">
                <label class="panel-title">Recent Comments ({{count($comments)}}):</label>
            </div>
            <div class="panel-body">
                @if (count($comments)>0)
                    <ul class="list-group"> 
                        @foreach ($comments as $comment)     
                            <li class="list-group-item comment_box" id="{{$comment->id}}">
                                <div class="row">
                                    <div class="col-xs-10 col-md-11">
                                        <div class="mic-info">
                                            <strong>{{$comment->user_name}}</strong><small><em> on </em>{{$comment->created_at}}</small>
                                        </div>                                
                                        <div class="comment-text" id="comment_text">{{$comment->comment_text}}</div>
                                        @if (Auth::user()->id == $comment->user_id)
                                            <div class="row">
                                                <form method="POST" action="{{url('/dashboard/delete/' . $comment->id)}}">
                                                    @csrf
                                                    <button type="button" class="btn btn-primary btn-xs" title="Edit" href="a">
                                                        <span class="glyphicon glyphicon-pencil"></span>
                                                    </button>
                                                </form>
                                                <form method="POST" action="{{url('/dashboard/delete/' . $comment->id)}}">
                                                    @csrf
                                                    <button type="submit" class="btn btn-danger btn-xs" title="Delete">
                                                        <span class="glyphicon glyphicon-trash"></span>
                                                    </button>
                                                </form>
                                            </div>
                                        @endif  
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
</div>

