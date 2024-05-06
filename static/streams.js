const APP_ID = 'd3a11fcb093442568faf26d9c8719c29'
const CHANNEL = 'main'
const TOKEN = '007eJxTYFD7GyevdaCj+9NGVbcrh58zblQy2XnlbGrP10U3Z+5avz5LgSHFONHQMC05ycDS2MTEyNTMIi0xzcgsxTLZwtzQMtnIsiDSMq0hkJHBTHQ2AyMUgvgsDLmJmXkMDADbYyCB'
let UID;

const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async () => {
    
    client.on('user-published', () => {
        console.log('User has joined our room!');
    })

    UID = await client.join(APP_ID, CHANNEL, TOKEN, null)

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let player = `<div class="video-container" id="user-container-${UID}">
                    <div class="username-wrapper"><span class="user-name">My Name</span></div>
                    <div class="video-player" id="user-${UID}"></div>
                </div>`
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])
}

joinAndDisplayLocalStream()