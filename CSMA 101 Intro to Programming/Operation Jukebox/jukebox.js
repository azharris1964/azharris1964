$(document).ready(function(){


	function Jukebox(current_song){
		var that = this;
		this.current_song = "";
		this.song_directory = [];
		this.song_names = [];
		this.play_list = [];
		queueClicker = 0;


//Shows a list of all of the songs in the Jukebox object
		this.song_display = function(){
			for (i in this.song_directory){
				this.song_names.push('<div class="song_item"><div class="circle"></div><a href="#" class="song_list" onClick="selectSong.call(this)" data-location="' + this.song_directory[i].location + '">' + this.song_directory[i].songName + '</a></div>');
			};
			$('#song_directory').html(this.song_names.join(" "));
		}


//finds the current_song location and returns the object in a variable
		this.findCurrentSong = function(){
			currentSong = this.current_song;
		}


//Adds a song to the Jukebox object
		this.add_song_to_directory = function(song3){
			this.song_directory.push(song3);
			return this.song_directory;
		};


//Grabs the song object location from the browser and displays the name of the current song 
		this.showCurrentSong = function(){
			for (i in this.song_directory){
				if (this.current_song == this.song_directory[i].location){
				  nowPlaying = this.song_directory[i].songName.toUpperCase(); 
				}
			}
			$('#current_song_playing').clearQueue().html("")
			showText(nowPlaying, 0);
		};

		var showText = function (message, index) { 
			if (index < message.length) {
		    $('#current_song_playing').append(message[index++]);
		    setTimeout(function () { showText(message, index, 300); }, 300);
		  }
		}

//Plays the current song
		playSong = function(){
			player.play();
		};


//Pauses the current song
		stopSong = function(){
			player.pause();
		};




//sets the queue 
		queueSong = function(){
			if (queueClicker == 0){
				queueClicker = 1;
			}
			else {
				queueClicker = 0;
			}
		};


//Grabs the current song from the browser and passes it to the change_song method
		selectSong = function(){
			var callingElement = this;
			this.current_song = callingElement;
		  var load_track = $(this).attr('data-location');
			if (queueClicker == 0){
			  that.change_song(load_track);
			}
			else {
				$('audio').on("ended", function(){
					if (queueClicker == 1){
						queueClicker = 0;
						that.change_song(load_track);
					};
				});
			};
		}



		this.change_song = function(str){
		  this.current_song = str;
			var str = str;
			audio = $("#player");
			$('source').remove();
			$('#player').append('<source src="' + str + '" type="audio/mpeg">');
			audio[0].pause();
			audio[0].load();
			audio[0].oncanplaythrough = audio[0].play();
			this.showCurrentSong();
		}

	};



	function Song(songName, title, location){
		this.songName = songName
		this.title = title;
		this.location = location;
	};



//CSS helper - a module will pop up to explain how to use the "queue" function
	$('.help').mouseover(function(){
		$('.popup').toggle();
	}).mouseout(function(){
		$('.popup').toggle();
	});




	Rap = new Song("Lil Uzi - XO Tour Llif3", "XO Tour Llif3.mp3", "audio/XO Tour Llif3.mp3");
	Pop = new Song("Cardi B -I Like It", "I Like It.mp3", "audio/I Like It.mp3");
	Rock = new Song("Imagine Dragons -Thunder", "Thunder.mp3", "audio/Thunder.mp3");
	Latin = new Song("Casper -Te Bote", "Te Bote.mp3", "audio/Te Bote.mp3");
	RB = new Song("Khalid - Love Lies", "Love Lies.mp3", "audio/Love Lies.mp3");
	EDM = new Song("Calvin Harris - One Kiss", "One Kiss.mp3", "audio/One Kiss.mp3");

  jukebox = new Jukebox(Rap);

	jukebox.add_song_to_directory(Rap);
	jukebox.add_song_to_directory(Pop);
	jukebox.add_song_to_directory(Rock);
	jukebox.add_song_to_directory(Latin);
	jukebox.add_song_to_directory(RB);
	jukebox.add_song_to_directory(EDM);



	jukebox.song_display();
	jukebox.showCurrentSong()
});