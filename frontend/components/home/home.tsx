import styles from './home.module.css';
import Image from 'next/image';

export default function About() {
	return (
        <section className={styles.container}>
            <div className={styles.body}>
                <p>
                    Fitness and Health Tracker is a Python-based application designed to 
                    help users monitor and analyze their physical activities, 
                    dietary habits, and other health metrics. The project leverages the 
                    Google Sheets API for easy data input and manipulation.
                </p>
            </div>
            <div className={styles.image}>
                <img src='/images/200w.gif' alt="Running Gif" />
            </div>
        </section>
    );
}