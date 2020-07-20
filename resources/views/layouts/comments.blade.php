<div class="container-fluid">
    <label class="label-primary">Comments</label>
    <form method="POST" action="{{url('/summaries/' . $summary[0]->summary_id .'/comment')}}">
        @csrf
        <input type="hidden" id="summary_id" name="summary id" value="{{$summary[0]->summary_id}}">
            <input type="hidden" id="summary_title" name="summary title" value="{{$summary[0]->summary_title}}">


        <div class="form-group">
            <div class="col-md-8">
                
                <input id="comment" type="text" class="form-control" name="comment_text">
                <button type="submit" class="btn btn-primary">
                    {{ __('Comment') }}
                </button>
            </div>
        </div>
    </form>
    
    <hr>

    <div class="container" id="comments">
        @if (count($comments)>0)
            <ul>
            @foreach ($comments as $comment)
                <li>
                    <label id="comment_user">{{$comment->user_name}}</label>
                    <small id="comment_text">{{$comment->created_at}}</small></br>
                    <p id="comment_text">{{$comment->comment_text}}</p>
                    
                </li>
            @endforeach
            </ul>
        @else
            <p>No comments yet</p>
        @endif

    </div>
</div>  