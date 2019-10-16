				var script = document.createElement('script');
				script.type='text/javascript';
				script.src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js";
				function onloadJquery()
				{
					$('head').append('<style>body {	margin: 0;	padding: 0;	background: transparent;	width: 160px;}div.ad_block {	display: table;	margin: 0 auto;	text-align: center;}div.hidden {	display: none;}</style>');
					var defaultRotateTime = 60; // Seconds to show next banner
					var ad_blocks = [{"content":"<iframe src=\"https:\/\/advert.livesportmedia.eu\/block\/right-7.php?id=374740\" framespacing=\"0\" frameborder=\"no\" scrolling=\"no\" style=\"width:160px;height:600px;\"><\/iframe>","content_type":"1","content_id":"0","timeout":"45","is_primary":"1"},{"content":"<A href=\"https:\/\/imstore.bet365affiliates.com\/Tracker.aspx?AffiliateId=9899&AffiliateCode=365_624163&CID=194&DID=63&TID=1&PID=149&LNG=1\" target=\"_blank\"><img src=\"https:\/\/imstore.bet365affiliates.com\/?AffiliateCode=365_624163&amp;CID=194&amp;DID=63&amp;TID=1&amp;PID=149&amp;LNG=1\" border=\"0\" \/><\/A>\r\n","content_type":"1","content_id":"0","timeout":"30","is_primary":"2"},{"content":"<iframe src=\"https:\/\/imstore.bet365affiliates.com\/365_624163-507-63-6-149-1-9899.aspx\" width=\"160\" height=\"600\" frameborder=\"0\" scrolling=\"no\">\r\n<\/iframe>","content_type":"1","content_id":"0","timeout":"30","is_primary":"2"}];
					var is_primary = 1;
					var ad_blocks_length = ad_blocks.length;
					var ad_keys = [];
					for(var i=0; i<ad_blocks_length; i++)
					{
						ad_keys[i] = i;
					}
					var all_ads_there = false;
					var actualAdId = 'ad_0';
					var documentWriteData = {};
					document.write = function(content)
					{
						if(typeof documentWriteData[actualAdId] == 'undefined')
						{
							documentWriteData[actualAdId] = '';
							setTimeout(document.writeFinish, 100);
						}
						documentWriteData[actualAdId] += content;
					};
					document.writeFinish = function()
					{
						data = documentWriteData[actualAdId];
						delete(documentWriteData[actualAdId]);
						$('#'+actualAdId).html(data);
					};

					rotate_content('first');

					function rotate_content(first)
					{
						shuffle(ad_keys, is_primary);
						var ad_num = 0;
						if(typeof(first) != 'undefined')
						{
							actualAdId = 'ad_'+(ad_keys[ad_num]);
							$("body").append('<div id="ad_'+(ad_keys[ad_num])+'" class="ad_block">'+ad_blocks[ad_keys[ad_num]]['content']+'</div>');
						}
						else
						{
							all_ads_there = true; // All adds are in html - initiate hidding rotation
						}

						var rotate_group = function(showBanner)
						{
							var rotateTime = ad_blocks[ad_keys[ad_num]].timeout;
							if (!rotateTime)
							{
								rotateTime = defaultRotateTime;
							}

							if (showBanner)
							{
								rotate_animation(ad_num);
							}

							ad_num++;

							if(ad_num == ad_blocks_length)
							{
								setTimeout(function(){
									rotate_content();
								}, rotateTime * 1000);
							}
							else
							{
								setTimeout(function(){
									rotate_group(true);
								}, rotateTime * 1000);
							}
						};
				
						rotate_group(all_ads_there);
					};

					function rotate_animation(ad_num)
					{
						$("body").animate({opacity:0}).queue(function()
						{
							$("body .ad_block").addClass('hidden');
							if(all_ads_there)
							{
								$("body div#ad_"+ad_keys[ad_num]).removeClass('hidden');
							}
							else
							{
								actualAdId = 'ad_'+(ad_keys[ad_num]);
								$("body").append('<div id="ad_'+(ad_keys[ad_num])+'" class="ad_block">'+ad_blocks[ad_keys[ad_num]]['content']+'</div>');
							}
							$(this).dequeue();
						}).animate({opacity:1});
					};

					function shuffle(array, is_primary) {
						var skip = is_primary ? 1 : 0;
						for (var i = array.length - 1 - skip; i > 0; i--) {
							var num = Math.floor(Math.random() * (i + 1) + skip);
							var d = array[num];
							array[num] = array[i];
							array[i] = d;
						}
						return array;
					};
				};

				if(script.addEventListener)
				{
					script.addEventListener("load", onloadJquery, false);
				}
				else if(script.readyState)
				{
					script.onreadystatechange = onloadJquery;
				}

				document.getElementsByTagName("head")[0].appendChild(script);
