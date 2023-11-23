import Link from 'next/link';
import React from 'react';
import styles from './navbar.module.css';

const Navigation = () => {
	return (
		<nav className={styles.navbar}>
			<Link href='/'>Health and Fitness Tracker</Link>
		</nav>
	);
};

export default Navigation;