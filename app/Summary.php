<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Summary extends Model
{
    public function comments(){
        return $this->hasMany('App\Comment');
    }
}
